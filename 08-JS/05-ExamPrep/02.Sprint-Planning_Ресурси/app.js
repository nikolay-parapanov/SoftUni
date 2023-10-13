window.addEventListener("load", solve);

function solve() {

    tasksCounter = 0;
    totalPoints = 0;

    const taskState = {
    title: null,
    description: null,
    label: null,
    points: null,
    assignee: null,
    taskId: null, 
    };

  const inputDOMSelectors = {
    title: document.getElementById("title"),
    description: document.getElementById("description"),
    label: document.getElementById("label"),
    points: document.getElementById("points"),
    assignee: document.getElementById("assignee"),
  };

  const otherDOMSelectors = {
    createTaskBtn: document.getElementById("create-task-btn"),
    deleteTaskBtn: document.getElementById("delete-task-btn"),
    taskSection: document.getElementById("tasks-section"),
    totalPointsSection: document.getElementById('total-sprint-points'),
  };

  otherDOMSelectors.createTaskBtn.addEventListener("click", createTaskHandler);

  function createTaskHandler() {
    console.log(inputDOMSelectors);
    const allFieldsHaveValue = Object.values(inputDOMSelectors).every(
      (input) => input.value !== ""
    );
    if (!allFieldsHaveValue) {
      console.log("missing field");
      return;
    }

    const { title, description, label, points, assignee } = inputDOMSelectors;
    for (const key in inputDOMSelectors) {
        taskState[key] = inputDOMSelectors[key].value;
    }
    tasksCounter += 1;
    taskState['taskId'] = tasksCounter;

    const article = createElement("article", otherDOMSelectors.taskSection, null, ["task-card"], `task-${tasksCounter}`, taskState);
    if (label.value === 'Feature'){
        createElement('div', article, `${label.value} &#8865`,['task-card-label', 'feature'] );
    } else if (label.value === 'Low Priority Bug'){
        createElement('div', article, `${label.value} &#9737;`,['task-card-label', 'low-priority'] );
    } else if (label.value === 'High Priority Bug'){
        createElement('div', article, `${label.value} &#9888;`,['task-card-label', 'high-priority'] );
    }
    createElement('h3', article, `${title.value}`, ['task-card-title']);
    createElement('p', article, `${description.value}`,['task-card-description']);
    createElement('div', article, `Estimated at ${points.value}`,['task-card-points']);
    createElement('div', article, `Assigned to: ${assignee.value}`,['task-card-assignee']);
    const actions = createElement('div', article, null, ['task-card-actions']);
    const deleteFromTaskListBtn = createElement('button', actions,'Delete' );

    deleteFromTaskListBtn.addEventListener('click', deleteTaskFromTaskListHandler);

    totalPoints += Number(points.value);
    setTotalPoints(totalPoints);
    
    clearAllInputs();
  }

  function setTotalPoints(points) {
    otherDOMSelectors.totalPointsSection.textContent = `Total Points ${points}pts`
  }

  function deleteTaskFromTaskListHandler(e){
    parentToBeDel = e.currentTarget.parentNode.parentNode;
    console.log(parentToBeDel);
    for (const key in inputDOMSelectors) {
        inputDOMSelectors[key].value = parentToBeDel.getAttribute(key);
    }

    taskId = parentToBeDel.getAttribute('id');
    console.log(taskId);

    otherDOMSelectors.createTaskBtn.setAttribute('disabled', true);
    otherDOMSelectors.deleteTaskBtn.removeAttribute('disabled');

    otherDOMSelectors.deleteTaskBtn.addEventListener('click', deleteTaskFromFormAndListHandler);
  }

  function deleteTaskFromFormAndListHandler(){
    itemToBeDeleted = document.getElementById(taskId);
    itemToBeDeleted.remove();

    totalPoints -= Number(itemToBeDeleted.getAttribute('points'));
    setTotalPoints(totalPoints);

    clearAllInputs();
}

  function clearAllInputs() {
    Object.values(inputDOMSelectors)
      .forEach((input) => {
        input.value = '';
      })
  }


  function createElement(
    type,
    parentNode,
    content,
    classes,
    id,
    attributes,
    useInnerHtml
  ) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
      htmlElement.innerHTML = content;
    } else {
      if (content && type !== "input") {
        htmlElement.textContent = content;
      }

      if (content && type === "input") {
        htmlElement.value = content;
      }
    }

    if (classes && classes.length > 0) {
      htmlElement.classList.add(...classes);
    }

    if (id) {
      htmlElement.id = id;
    }

    // { src: 'link', href: 'http' }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}
