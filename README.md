# 📦 Warehouse Activity Analysis & Visualization Demo

> **Disclaimer**: This is a **demo** version. The full project resides in the company’s internal repository and is not included here.  
> I created this demo to present to stakeholders and evaluate different visualization approaches before final implementation.

This demo showcases how warehouse activity data can be visualized using an **interactive 3D heatmap** or a **2D-projected 3D layout**, offering valuable insights for warehouse optimization. While this version focuses on **pick frequency**, the complete project will support broader analyses and richer features.

### 🔀 Branches
- **`main`** — Interactive 3D visualization
- **`2D`** — Alternative 2D-projected visualization

---

## 📈 Full Project Objectives

- Optimize warehouse layout and slotting
- Visualize both current and forecasted inventory levels
- Support labor planning using pick demand heatmaps
- Identify bottlenecks and congestion areas

---

## 🔍 Overview

- **Visualization**: Pick locations are color-coded from **red (most picked)** to **blue (least picked)**.
- **Input Data**: Sample or live pick frequency data with location references
- **Output**: Interactive 3D or 2D model with hover tooltips for pick stats and hotspot visibility

---

## 🛠 Features

- Customizable warehouse rack structure and bin configurations
- Easy integration with existing WMS or analytics pipelines
- Interactive drill-down for visualizing high-activity zones
- 2D fallback for quick overview or lower resource consumption

---

## 📷 Sample Output

### 🔺 3D Visualization

👉 [Interactive Demo (HTML)](https://github.com/AyubSherif/WarehouseManagementAppDemo/blob/main/img/3d_warehouse_visualization.html)

**Snapshot**

![3D Snapshot](https://github.com/AyubSherif/WarehouseManagementAppDemo/blob/main/img/3D%20demo.png)

---

### 🔻 2D Visualization

👉 [Interactive Demo (HTML)](https://github.com/AyubSherif/WarehouseManagementAppDemo/blob/main/img/2d_warehouse_visualization.html)


![2D Snapshot](https://github.com/AyubSherif/WarehouseManagementAppDemo/blob/main/img/2D%20demo.png)

---

## 🚀 Getting Started

1. Clone the repository
2. Install Python dependencies (see `requirements.txt`)
3. Load or simulate a pick frequency table
4. Run the main script to generate and interact with the visualization

---

## 🧠 Full Project Enhancements (Planned)

> These features are **not** implemented in the current demo, but are part of full project:

- Dynamic layouts from external config files
- Zoom-based aggregation (e.g., group bins when zoomed out)
- Z-axis aggregation for bird’s-eye views
- Real-time pick tracking
- Date range filtering
- Switchable statistic overlays (e.g., picks, replenishments, velocity)