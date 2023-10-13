function sprint(input) {
  let n = Number(input.shift());

  let tasks = {};
  let assignees = {};

  for (let index = 0; index < n; index++) {
    const [assignee, taskId, title, status, estimatedPoints] = input
      .shift()
      .split(":");
    tasks[taskId] = { assignee, title, status, estimatedPoints };
    if (!assignees.hasOwnProperty(assignee)) {
      assignees[assignee] = [taskId];
    } else {
      assignees[assignee].push(taskId);
    }
  }

  for (let inputLine of input) {
    if (inputLine === "Stop") {
      break;
    }

    let commandTokens = inputLine.split(":");
    let command = commandTokens[0];

    if (command === "Add New") {
      let [assignee, taskId, title, status, estimatedPoints] =
        commandTokens.slice(1);
      if (!assignees.hasOwnProperty(assignee)) {
        console.log(`Assignee ${assignee} does not exist on the board!`);
      } else {
        assignees[assignee].push(taskId);
        tasks[taskId] = { assignee, title, status, estimatedPoints };
      }
    } else if (command === "Change Status") {
      let [assignee, taskId, newStatus] = commandTokens.slice(1);
      if (!assignees.hasOwnProperty(assignee)) {
        console.log(`Assignee ${assignee} does not exist on the board!`);
      } else if (!assignees[assignee].includes(taskId)) {
        console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
      } else {
        tasks[taskId].status = newStatus;
      }
    } else if (command === "Remove Task") {
      let [assignee, index] = commandTokens.slice(1);
      if (!assignees.hasOwnProperty(assignee)) {
        console.log(`Assignee ${assignee} does not exist on the board!`);
      } else if (index < 0 || index >= assignees[assignee].length) {
        console.log(`Index is out of range!`);
      } else {
        let taskId = assignees[assignee][index];
        delete tasks[taskId];
        assignees[assignee].splice(index, 1);
      }
    }
  }

  let toDoTasksTotalPoints = 0;
  let inProgressTasksTotalPoints = 0;
  let codeReviewTasksTotalPoints = 0;
  let doneTasksTotalPoints = 0;

  for (const taskId in tasks) {
    if (tasks[taskId].status === "ToDo") {
      toDoTasksTotalPoints += Number(tasks[taskId].estimatedPoints);
    } else if (tasks[taskId].status === "In Progress") {
      inProgressTasksTotalPoints += Number(tasks[taskId].estimatedPoints);
    } else if (tasks[taskId].status === "Code Review") {
      codeReviewTasksTotalPoints += Number(tasks[taskId].estimatedPoints);
    } else if (tasks[taskId].status === "Done") {
      doneTasksTotalPoints += Number(tasks[taskId].estimatedPoints);
    }
  }

  console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
  console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
  console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
  console.log(`Done Points: ${doneTasksTotalPoints}pts`);

  if (
    doneTasksTotalPoints >=
    toDoTasksTotalPoints +
      inProgressTasksTotalPoints +
      codeReviewTasksTotalPoints
  ) {
    console.log(`Sprint was successful!`);
  } else {
    console.log(`Sprint was unsuccessful...`);
  }
}
