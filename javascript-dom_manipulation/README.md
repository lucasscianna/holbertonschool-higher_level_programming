# JavaScript - DOM Manipulation

## Description

This project explores the fundamentals of **DOM (Document Object Model) manipulation** using vanilla JavaScript. The goal is to interact with HTML elements dynamically — without reloading the page — by selecting, modifying, and listening to events on DOM nodes, as well as fetching external data via network requests.

---

## Resources

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)
- [CSS Diner – Play with Selectors](https://flukeout.github.io/)
- [DOM Scripting](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Network Requests](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

---

## Learning Objectives

By the end of this project, you should be able to explain — without any external help — the following concepts:

### DOM Selection
- How to select HTML elements in JavaScript
- The differences between **ID**, **class**, and **tag name** selectors

### DOM Manipulation
- How to modify an HTML element's **style**
- How to **get and update** an HTML element's content
- How to **modify the DOM** (add, remove, or update elements)

### Network Requests
- How to make a request using **XMLHttpRequest**
- How to make a request using the **Fetch API**

### Events
- How to **listen/bind to DOM events**
- How to **listen/bind to user events** (clicks, inputs, etc.)

---

## Requirements

| Requirement | Detail |
|---|---|
| Allowed editors | All editors (VSCode, Vim, Emacs, etc.) |
| Browser | Chrome version 57.0 or later |
| File endings | All files must end with a new line |
| README | Mandatory `README.md` at the root of the project |
| Code style | Must be `semistandard` compliant |
| Variable declarations | `var` is **not allowed** — use `const` or `let` |
| Page reloads | HTML must **not reload** for any action (DOM manipulation, value updates, data fetching) |

---

## Key Concepts

### Selectors

```javascript
// By ID
const el = document.getElementById('my-id');

// By class name
const els = document.getElementsByClassName('my-class');

// By tag name
const tags = document.getElementsByTagName('div');

// CSS selector (single)
const el = document.querySelector('.my-class #my-id');

// CSS selector (all matches)
const els = document.querySelectorAll('ul > li');
```

### Modifying Style & Content

```javascript
// Change style
el.style.color = 'red';

// Get/set text content
el.textContent = 'Hello, World!';

// Get/set HTML content
el.innerHTML = '<strong>Bold text</strong>';
```

### Network Requests

```javascript
// XMLHttpRequest
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data');
xhr.onload = () => console.log(xhr.responseText);
xhr.send();

// Fetch API
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

### Event Listeners

```javascript
// DOM event
document.addEventListener('DOMContentLoaded', () => {
  console.log('DOM fully loaded');
});

// User event
const btn = document.querySelector('#my-btn');
btn.addEventListener('click', () => {
  console.log('Button clicked!');
});
```

---

## Author

Project completed as part of the **Holberton School** curriculum.