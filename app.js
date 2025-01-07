document.addEventListener("DOMContentLoaded", () => {
  const branchesContainer = document.getElementById("branches");
  const salesForm = document.getElementById("sales-form");

  // Fetch branches data
  fetch("http://127.0.0.1:8000/api/branches/")
    .then((response) => response.json())
    .then((branches) => {
      branches.forEach((branch) => {
        const branchCard = document.createElement("div");
        branchCard.innerHTML = `
          <h3>${branch.name}</h3>
          <p>Location: ${branch.location}</p>
        `;
        branchesContainer.appendChild(branchCard);
      });
    });

  // Handle sales form submission
  salesForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(salesForm);
    const data = Object.fromEntries(formData);

    fetch("http://127.0.0.1:8000/api/sales/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        alert("Sales recorded successfully!");
        salesForm.reset();
      })
      .catch((error) => alert("Error recording sales."));
  });
});
