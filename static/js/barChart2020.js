const MARGIN = { LEFT: 100, RIGHT: 10, TOP: 10, BOTTOM: 130 };
const WIDTH = 900 - MARGIN.LEFT - MARGIN.RIGHT;
const HEIGHT = 400 - MARGIN.TOP - MARGIN.BOTTOM;

const svg = d3
  .select("#barChart2020")
  .append("svg")
  .attr("width", WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
  .attr("height", HEIGHT + MARGIN.TOP + MARGIN.BOTTOM);

const g = svg
  .append("g")
  .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`);

group = "2020";

function getPercentage(datasetBarChart) {
  console.log(datasetBarChart);
  return datasetBarChart.filter((d) => d.group === group);
}

function d3BarChart2020(datasetBarChart) {
  defaultBarChart = getPercentage(datasetBarChart);

  const x = d3
    .scaleBand()
    .domain(defaultBarChart.map((d) => d.category))
    .range([0, WIDTH])
    .paddingInner(0.4)
    .paddingOuter(0.2);

  const y = d3
    .scaleLinear()
    .domain([0, d3.max(defaultBarChart, (d) => d.value)])
    .range([HEIGHT, 0]);

  //define axis

  const xAxisCall = d3.axisBottom(x);
  g.append("g")
    .attr("class", "x axis")
    .attr("transform", `translate(0, ${HEIGHT})`)
    .call(xAxisCall);

  const yAxisCall = d3.axisLeft(y);
  g.append("g").attr("class", "y axis").call(yAxisCall);

  const rects = g.selectAll("rect").data(defaultBarChart);
  rects.enter();
  rects
    .enter()
    .append("rect")
    .attr("x", (d) => x(d.category))
    .attr("y", (d) => y(d.value))
    .attr("width", x.bandwidth())
    .attr("height", (d) => HEIGHT - y(d.value))
    .attr("fill", "grey");
}
