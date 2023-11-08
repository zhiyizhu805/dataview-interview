const urls = [pieChartDataUrl, barChartDataUrl];
// console.log("urls", urls);

Promise.all(urls.map((url) => d3.json(url))).then(run);

function run(dataset) {
  //   console.log("dataset", dataset);
  d3PieChart(dataset[0], dataset[1]);
  d3BarChart(dataset[1]);
  d3BarChart2020(dataset[1]);
}
