/*
  AI IMP NEWS OS
  Content Queue Script
*/

document.addEventListener("DOMContentLoaded", function() {

    loadQueues();

    // Tab switching
    document.querySelectorAll(".tabs .tab").forEach(tab => {
        tab.addEventListener("click", function() {
            const queue = this.getAttribute("data-queue");
            document.querySelectorAll(".tabs .tab").forEach(t => t.classList.remove("active"));
            document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
            this.classList.add("active");
            document.getElementById(`tab-${queue}`).classList.add("active");
        });
    });

    const refreshBtn = document.getElementById("btn-refresh");
    if (refreshBtn) {
        refreshBtn.addEventListener("click", function() {
            loadQueues();
            showToast("Queue Refreshed", "success");
        });
    }

    setInterval(loadQueues, 30000);
});

async function loadQueues() {
    const data = await API.getQueue();
    if (!data) return;

    const publishList = data.publish_queue || [];
    const rewriteList = data.rewrite_queue || [];

    document.getElementById("cq-publish").textContent = publishList.length;
    document.getElementById("cq-rewrite").textContent = rewriteList.length;

    renderQueue("publish-queue-grid", publishList);
    renderQueue("rewrite-queue-grid", rewriteList);
}

function renderQueue(gridId, items) {
    const grid = document.getElementById(gridId);
    if (!grid) return;

    if (items.length === 0) {
        grid.innerHTML = `<div class="empty-state">
            <div class="empty-state-icon">📭</div>
            <div class="empty-state-text">कोई Article नहीं मिला</div>
        </div>`;
        return;
    }

    grid.innerHTML = items.map(item => `
        <div class="queue-item-card">
            <div class="queue-item-content">
                <div class="queue-item-title">${item.title || "No Title"}</div>
                <div class="queue-item-meta">
                    <span>📰 ${item.source || "Unknown"}</span>
                    <span>📂 ${item.category || "General"}</span>
                    <span>📅 ${item.run_date}</span>
                    <span>${getDecisionBadge(item.decision)}</span>
                </div>
            </div>
            <div class="queue-item-stats">
                <div class="queue-stat">
                    <div class="queue-stat-value">${item.quality_score}</div>
                    <div class="queue-stat-label">Quality</div>
                </div>
                <div class="queue-stat">
                    <div class="queue-stat-value">${item.confidence}%</div>
                    <div class="queue-stat-label">Confidence</div>
                </div>
            </div>
        </div>
    `).join("");
}