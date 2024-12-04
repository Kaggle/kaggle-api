install<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Carrefour Weekly Performance Report</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }
    
    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
    }
    
    th, td {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
    
    th {
      background-color: #f2f2f2;
    }
    
    .kpi-card {
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 15px;
      margin-bottom: 20px;
    }
    
    .kpi-card h3 {
      margin-top: 0;
    }
    
    .kpi-value {
      font-size: 24px;
      font-weight: bold;
    }
    
    .trend-icon {
      margin-right: 5px;
    }
    
    .trend-up {
      color: green;
    }
    
    .trend-down {
      color: red;
    }
  </style>
</head>
<body>
  <h1>Carrefour Weekly Performance Report</h1>
  <p>Date: 24/11/2024</p>
  
  <div class="kpi-card">
    <h3>Daily Sales</h3>
    <div class="kpi-value">₪152,000</div>
    <div class="trend">
      <span class="trend-icon trend-down">▼</span>
      -27.8% vs. Last Year
    </div>
  </div>
  
  <div class="kpi-card">
    <h3>Average Basket Size</h3>
    <div class="kpi-value">₪177</div>
    <div class="trend">
      <span class="trend-icon trend-down">▼</span>
      -33.2% vs. Average
    </div>
  </div>
  
  <div class="kpi-card">
    <h3>Online Sales</h3>
    <div class="kpi-value">₪26,000</div>
    <div class="trend">
      <span class="trend-icon trend-down">▼</span>
      -7.7% vs. Average
    </div>
  </div>
  
  <h2>Department Performance</h2>
  <table>
    <thead>
      <tr>
        <th>Department</th>
        <th>Performance vs. Average</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Meat & Fish</td>
        <td class="trend-up">+10.6%</td>
        <td class="trend-up">Strong</td>
      </tr>
      <tr>
        <td>Produce</td>
        <td class="trend-down">-24.1%</td>
        <td class="trend-down">Weak</td>
      </tr>
      <tr>
        <td>Dairy & Frozen</td>
        <td class="trend-down">-15.7%</td>
        <td class="trend-down">Weak</td>
      </tr>
      <tr>
        <td>Grocery</td>
        <td class="trend-down">-10.4%</td>
        <td class="trend-down">Weak</td>
      </tr>
      <tr>
        <td>Beverages</td>
        <td class="trend-down">-33.0%</td>
        <td class="trend-down">Critical</td>
      </tr>
    </tbody>
  </table>
  
  <h2>Recommendations</h2>
  <ul>
    <li>Implement targeted promotions and pricing adjustments for underperforming departments (Produce, Dairy & Frozen, Beverages)</li>
    <li>Enhance customer experience in fresh departments to drive sales</li>
    <li>Analyze online sales performance and identify opportunities to improve conversion and average order value</li>
    <li>Monitor labor efficiency and adjust staffing levels to match traffic patterns</li>
  </ul>
</body>
</html>
