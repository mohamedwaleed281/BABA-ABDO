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
