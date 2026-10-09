"""
AI IMP NEWS OS
Master Pipeline Orchestrator
Version: 2.0

7-Stage Full Autonomous Pipeline:
Stage 0: Database & Schema Setup
Stage 1: News Collector Agent (RSS)
Stage 2: IMP News Selector Agent (Top 6)
Stage 3: Verify Source Agent (Verification & Evidence)
Stage 4: Human Writer Boss (Hook, Story, Fact, Tone, CTA)
Stage 5: SEO & Image Agent (Slug, Prompts, Media)
Stage 6: Publish Agent (Local Publisher)
Stage 7: Final Boss QA Inspection Agent (Approval Check)
"""

from datetime import datetime

from app.database.schema import create_tables
from app.agents.news_collector.collector import NewsCollectorAgent
from app.agents.verify_source.verify import VerifySourceAgent
from app.agents.human_writer.boss import HumanWriterBoss
from app.agents.publish.publish_agent import PublishAgent
from app.agents.final_boss.qa_agent import FinalBossQAAgent
from app.services.queue_manager.manager import QueueManager


def run_pipeline():
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + "=" * 70)
    print(f"🚀 AI IMP NEWS OS — MASTER PIPELINE RUN [Started: {today}]")
    print("=" * 70)

    # PHASE 0: Database Setup
    print("\nPHASE 0: DATABASE & SCHEMA SETUP")
    print("-" * 70)
    create_tables()

    # PHASE 1: News Collector Agent (RSS)
    print("\nPHASE 1: NEWS COLLECTOR AGENT")
    print("-" * 70)
    collector = NewsCollectorAgent()
    collector.run()

    # PHASE 2 & 3: Verify Source Agent (Selector + Verification)
    print("\nPHASE 2 & 3: SELECTOR & VERIFY SOURCE AGENT")
    print("-" * 70)
    verifier = VerifySourceAgent()
    verifier.run()

    # PHASE 4 & 5: Human Writer Boss (Content + Image + SEO)
    print("\nPHASE 4 & 5: HUMAN WRITER BOSS (CONTENT + IMAGE + SEO)")
    print("-" * 70)
    writer_boss = HumanWriterBoss()
    writer_results = writer_boss.run()

    # PHASE 6: Queue Manager & Publish Agent
    print("\nPHASE 6: QUEUE MANAGER & PUBLISH AGENT")
    print("-" * 70)
    queue = QueueManager()
    queue.run()

    publisher = PublishAgent()
    publisher.run()

    # PHASE 7: Final Boss QA Inspection
    print("\nPHASE 7: FINAL BOSS / QA INSPECTION AGENT")
    print("-" * 70)
    final_boss = FinalBossQAAgent()
    final_boss.run()

    print("\n" + "=" * 70)
    print(f"🏆 MASTER PIPELINE COMPLETE SUCCESS [Completed: {datetime.now().strftime('%H:%M:%S')}]")
    print("=" * 70 + "\n")

    return writer_results


if __name__ == "__main__":
    run_pipeline()