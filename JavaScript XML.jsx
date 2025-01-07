 restaurant-management-frontend/
├── src/
│   ├── components/
│   │   ├── Dashboard.js
│   │   ├── Sales.js
│   │   ├── Inventory.js
│   │   ├── Expenses.js
│   │   ├── Recommendations.js
│   │   ├── Alerts.js
│   ├── App.js
│   ├── index.js




import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import Sales from "./components/Sales";
import Inventory from "./components/Inventory";
import Expenses from "./components/Expenses";
import Recommendations from "./components/Recommendations";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/sales" element={<Sales />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/expenses" element={<Expenses />} />
        <Route path="/recommendations" element={<Recommendations />} />
      </Routes>
    </Router>
  );
}

export default App;


import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [branches, setBranches] = useState([]);

  useEffect(() => {
    axios.get("/api/branches/").then((response) => {
      setBranches(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      {branches.map((branch) => (
        <div key={branch.id}>
          <h2>{branch.name}</h2>
          <p>{branch.location}</p>
        </div>
      ))}
    </div>
  );
};

export default Dashboard;


import React, { useState } from "react";
import axios from "axios";

const Sales = () => {
  const [formData, setFormData] = useState({
    branch: "",
    total_orders: 0,
    total_revenue: 0.0,
    payment_method: "Cash",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("/api/sales/", formData).then(() => {
      alert("Sale recorded successfully!");
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Record Sales</h1>
      <input
        type="number"
        placeholder="Total Orders"
        onChange={(e) => setFormData({ ...formData, total_orders: e.target.value })}
      />
      <input
        type="number"
        placeholder="Total Revenue"
        onChange={(e) => setFormData({ ...formData, total_revenue: e.target.value })}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default Sales;




