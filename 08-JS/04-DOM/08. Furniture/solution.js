function solve() {
  const [generateTextArea, buyTextArea] = Array.from(
    document.getElementsByTagName("textarea")
  );
  const [generateBtn, buyBtn] = Array.from(
    document.getElementsByTagName("button")
  );
  const tbody = document.querySelector(".table > tbody");

  generateBtn.addEventListener("click", generateHandler);
  buyBtn.addEventListener("click", buyHandler);

  function generateHandler() {
    const data = JSON.parse(generateTextArea.value);
    for (const { img, name, price, decFactor } of data) {
      const tableRow = createElement("tr", "", tbody);
      const firstColTd = createElement("td", "", tableRow);
      createElement("img", "", firstColTd, "", "", { src: img });
      const secondColTd = createElement("td", "", tableRow);
      createElement("p", name, secondColTd);
      const thirdColTd = createElement("td", "", tableRow);
      createElement("p", price, thirdColTd);
      const fourthColTd = createElement("td", "", tableRow);
      createElement("p", decFactor, fourthColTd);
      const fifthColTd = createElement("td", "", tableRow);
      createElement("input", "", fifthColTd, "", "", { type: "checkbox" });
    }
  }

  function buyHandler() {
    const allCheckedInputs = Array.from(
      document.querySelectorAll("tbody tr input:checked")
    );

    let boughtItems = [];
    let totalPrice = 0;
    let totalDecFactor = 0;

    for (const input of allCheckedInputs) {
      const tableRow = input.parentElement.parentElement;
      const [_firstCol, secondCol, thirdCol, fourthCol] = Array.from(
        tableRow.children
      );
      let item = secondCol.children[0].textContent;
      boughtItems.push(item);
      let currentPrice = Number(thirdCol.children[0].textContent);
      totalPrice += currentPrice;
      let currentDecFactor = Number(fourthCol.children[0].textContent);
      totalDecFactor += currentDecFactor;
    }
    buyTextArea.value += `Bought furniture: ${boughtItems.join(", ")}\n`;
    buyTextArea.value += `Total price: ${totalPrice.toFixed(2)}\n`;
    buyTextArea.value += `Average decoration factor: ${
      totalDecFactor / allCheckedInputs.length
    }\n`;
  }

  // type = string
  // content = string (text content)
  // id = string
  // classes = array of strings
  // attributes = object

  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    if (id) {
      htmlElement.id = id;
    }

    if (classes) {
      htmlElement.classList.add(...classes);
    }

    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    return htmlElement;
  }
}
