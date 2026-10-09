/*
  AI IMP NEWS OS
  Central API Handler
  Version: 2.0
*/

const API_BASE = "http://127.0.0.1:8000";

const API = {

    // ===== DASHBOARD =====
    async getStats() {
        try {
            const res = await fetch(`${API_BASE}/api/stats`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getStats failed:", err);
            return null;
        }
    },

    async getQueue() {
        try {
            const res = await fetch(`${API_BASE}/api/queue`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getQueue failed:", err);
            return null;
        }
    },

    async getPipelineStatus() {
        try {
            const res = await fetch(`${API_BASE}/api/pipeline`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getPipelineStatus failed:", err);
            return null;
        }
    },

    // ===== PIPELINE JOURNEY =====
    async getRawNews() {
        try {
            const res = await fetch(`${API_BASE}/api/journey/raw-news`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getRawNews failed:", err);
            return null;
        }
    },

    async getJourneyDates() {
        try {
            const res = await fetch(`${API_BASE}/api/journey/dates`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getJourneyDates failed:", err);
            return null;
        }
    },

    async getJourney(runDate) {
        try {
            const url = (runDate && runDate !== "latest")
                ? `${API_BASE}/api/journey/${runDate}`
                : `${API_BASE}/api/journey/latest/full`;
            const res = await fetch(url);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getJourney failed:", err);
            return null;
        }
    },

    // ===== ANALYTICS =====
    async getAnalytics(days) {
        try {
            const res = await fetch(`${API_BASE}/api/analytics/summary?days=${days || 7}`);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.getAnalytics failed:", err);
            return null;
        }
    },

    // ===== RUN PIPELINE =====
    async runPipeline() {
        try {
            const res = await fetch(`${API_BASE}/api/run-pipeline`, { method: "POST" });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            console.error("API.runPipeline failed:", err);
            return null;
        }
    }
};