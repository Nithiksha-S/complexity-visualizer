function loadData() {
    let n = document.getElementById("nInput").value;

    fetch(`/compute?n=${n}`)
        .then(res => res.json())
        .then(data => {

            let html = "<table>";

            html += `
                <tr>
                    <th>n</th>
                    <th>O(1)</th>
                    <th>O(log n)</th>
                    <th>O(n)</th>
                    <th>O(n log n)</th>
                    <th>O(n²)</th>
                </tr>
            `;

            for (let i = 0; i < data.x.length; i++) {
                html += `
                    <tr>
                        <td>${data.x[i]}</td>
                        <td>${data["O(1)"][i]}</td>
                        <td>${data["O(log n)"][i]}</td>
                        <td>${data["O(n)"][i]}</td>
                        <td>${data["O(n log n)"][i]}</td>
                        <td>${data["O(n^2)"][i]}</td>
                    </tr>
                `;
            }

            html += "</table>";

            document.getElementById("output").innerHTML = html;
        });
}