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
