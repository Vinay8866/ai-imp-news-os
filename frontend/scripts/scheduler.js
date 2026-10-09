/*
  AI IMP NEWS OS
  Scheduler Page Script
  Version: 2.0
*/

document.addEventListener("DOMContentLoaded", function() {

    // Run Now button
    const runNowBtn = document.getElementById("btn-run-now");
    if (runNowBtn) {
        runNowBtn.addEventListener("click", async function() {
            showToast("Starting pipeline...", "info");
            runNowBtn.disabled = true;
            runNowBtn.textContent = "⏳ Running...";

            const result = await API.runPipeline();

            if (result) {
                showToast("Pipeline completed!", "success");
            } else {
                showToast("Pipeline failed. Check backend.", "error");
            }

            runNowBtn.disabled = false;
            runNowBtn.textContent = "▶ Run Pipeline Now";
        });
    }

    // Save Schedule button (placeholder)
    const saveBtn = document.getElementById("btn-save-schedule");
    if (saveBtn) {
        saveBtn.addEventListener("click", function() {
            showToast("Schedule saved successfully!", "success");
        });
    }

    // Pause button (placeholder)
    const pauseBtn = document.getElementById("btn-pause");
    if (pauseBtn) {
        pauseBtn.addEventListener("click", function() {
            showToast("Scheduler paused", "warning");
        });
    }
});