"""
AI IMP NEWS OS
FastAPI REST Endpoints
Version: 2.0

Frontend (HTML/CSS/JS) के लिए सारे Endpoints:
- /api/stats
- /api/queue
- /api/pipeline
- /api/journey/raw-news
- /api/journey/dates
- /api/journey/{run_date}
- /api/journey/latest/full
- /api/run-pipeline (Triggers complete 7-agent pipeline)
"""

from datetime import datetime
from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.database.repository import OutputRepository, NewsRepository
from app.database.pipeline_repo import PipelineStagesRepository


router = APIRouter()
output_db = OutputRepository()
news_db = NewsRepository()
stages_db = PipelineStagesRepository()


@router.get("/api/stats")
def get_stats():
    """Dashboard Stats Summary"""
    today = datetime.now().strftime("%Y-%m-%d")
    summary = output_db.today_summary(today)

    total = summary.get("total") or 0
    rewrite_count = summary.get("rewrite_count") or 0
    pending_queue = output_db.get_publish_queue()
    published_today = output_db.get_published_count(today)

    return {
        "running_agents": 7,
        "todays_news": total,
        "publish_queue": len(pending_queue),
        "published_today": published_today,
        "failed_jobs": rewrite_count,
        "avg_quality": round(summary.get("avg_quality") or 0, 1),
        "avg_confidence": round(summary.get("avg_confidence") or 0, 1)
    }


@router.get("/api/queue")
def get_queue():
    """Content Queue Items"""
    publish_items = output_db.get_publish_queue()
    rewrite_items = output_db.get_rewrite_queue()
    return {
        "publish_queue": publish_items,
        "rewrite_queue": rewrite_items
    }


@router.get("/api/pipeline")
def get_pipeline_status():
    """Live Pipeline Nodes Status"""
    today = datetime.now().strftime("%Y-%m-%d")
    counts = stages_db.count_by_stage(today)

    has_data = (counts.get("total") or 0) > 0
    has_selected = (counts.get("selected") or 0) > 0
    has_verified = (counts.get("verified") or 0) > 0
    has_humanized = (counts.get("humanized") or 0) > 0
    has_image = (counts.get("with_image") or 0) > 0
    has_published = (counts.get("published") or 0) > 0

    return {
        "rss": "success" if has_data else "pending",
        "imp_news": "success" if has_selected else "pending",
        "verify": "success" if has_verified else "pending",
        "writer": "success" if has_humanized else "pending",
        "image": "success" if has_image else "pending",
        "publish": "success" if has_published else "pending"
    }


@router.get("/api/journey/raw-news")
def get_raw_news():
    """Stage 1: All Raw RSS Articles"""
    articles = news_db.latest(limit=50)
    return {
        "raw_news": articles,
        "total": len(articles)
    }


@router.get("/api/journey/dates")
def get_journey_dates():
    """Available Run Dates"""
    dates = stages_db.get_all_dates(limit=30)
    return {"dates": dates}


@router.get("/api/journey/latest/full")
def get_latest_journey():
    """Latest Run Complete Journey"""
    latest_date = stages_db.get_latest_run_date()
    if not latest_date:
        return {"run_date": None, "journey": [], "total": 0}
    journey = stages_db.get_journey(latest_date)
    return {
        "run_date": latest_date,
        "journey": journey,
        "total": len(journey)
    }


@router.get("/api/journey/{run_date}")
def get_journey_by_date(run_date: str):
    """Specific Date Journey"""
    journey = stages_db.get_journey(run_date)
    return {
        "run_date": run_date,
        "journey": journey,
        "total": len(journey)
    }


@router.get("/api/analytics/summary")
def get_analytics_summary(days: int = 7):
    """Analytics Summary"""
    runs = output_db.get_all_runs(days=days)
    return {
        "days": days,
        "runs": runs,
        "total_runs": len(runs)
    }


@router.post("/api/run-pipeline")
def trigger_pipeline(background_tasks: BackgroundTasks):
    """
    Triggers complete Master Pipeline in background or synchronously
    """
    from app.main import run_pipeline
    try:
        results = run_pipeline()
        return {
            "status": "success",
            "message": "Pipeline completed successfully!",
            "processed_count": len(results) if results else 0
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))