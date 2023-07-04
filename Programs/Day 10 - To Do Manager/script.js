var tasks = [];

function addTask() {
  var input = document.getElementById("taskInput");
  var task = input.value;
  input.value = "";

  if (task === "") {
    alert("Please enter a task!");
    return;
  }

  var dueDate = prompt("Enter the due date (DD-MM-YYYY):");
  if (dueDate === null || dueDate === "") {
    alert("Please enter a due date!");
    return;
  }

  var newTask = {
    title: getTaskTitle(task, dueDate),
    description: "",
    dueDate: parseDueDate(dueDate),
    priority: "",
    completed: false
  };

  tasks.push(newTask);
  renderTasks();
}

function getTaskTitle(task, dueDate) {
  var now = new Date();
  var parsedDueDate = parseDueDate(dueDate);
  var timeDiff = parsedDueDate.getTime() - now.getTime();
  var daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

  if (daysDiff === 0) {
    return task + " (Due Today)";
  } else if (daysDiff < 0) {
    return task + " (Overdue)";
  } else {
    return task + " (Due in " + daysDiff + " days)";
  }
}

function parseDueDate(dueDate) {
  var parts = dueDate.split("-");
  var day = parseInt(parts[0], 10);
  var month = parseInt(parts[1], 10) - 1;
  var year = parseInt(parts[2], 10);
  return new Date(year, month, day);
}

function renderTasks() {
  var taskList = document.getElementById("taskList");
  taskList.innerHTML = "";

  for (var i = 0; i < tasks.length; i++) {
    var task = tasks[i];

    var li = document.createElement("li");
    li.className = task.completed ? "completed" : "";

    var span = document.createElement("span");
    span.appendChild(document.createTextNode(task.title));
    li.appendChild(span);

    var deleteButton = document.createElement("button");
    deleteButton.appendChild(document.createTextNode("Delete"));
    deleteButton.onclick = createDeleteHandler(i);
    li.appendChild(deleteButton);

    var completeButton = document.createElement("button");
    completeButton.appendChild(document.createTextNode("Complete"));
    completeButton.onclick = createCompleteHandler(i);
    li.appendChild(completeButton);

    taskList.appendChild(li);
  }
}

function createDeleteHandler(index) {
  return function() {
    deleteTask(index);
  };
}

function createCompleteHandler(index) {
  return function() {
    toggleCompletion(index);
  };
}

function deleteTask(index) {
  tasks.splice(index, 1);
  renderTasks();
}

function toggleCompletion(index) {
  tasks[index].completed = !tasks[index].completed;
  renderTasks();
}
