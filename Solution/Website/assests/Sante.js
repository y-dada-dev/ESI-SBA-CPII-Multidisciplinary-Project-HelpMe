// import {Modal} from "./Packages/bootstrap/bootstrap";



/* -- Navigation Bar -------------------------------------------------------------------- */
var openMenucategories = document.querySelector(".open-menu-categories");
var categoriesMenu = document.querySelector(".categories");
var selectedcategories = document.querySelector(".selected-categories");
var closeMenucategories = document.querySelector(".close-menu-categories");
var accountButton = document.querySelector(".accueil_button");
var associationButton = document.querySelector(".association_button");

openMenucategories.onmouseover = categories;

function categories() {
  close();
  categoriesMenu.style.display = "block";
  selectedcategories.classList.add("selected-rotate");
}

var closer = document.querySelector(".carousel");

closeMenucategories.onclick = close;
closer.onmouseover = close;
accountButton.onmouseover = close;
associationButton.onmouseover = close;

function close() {
  categoriesMenu.style.display = "none";
  selectedcategories.classList.remove("selected-rotate");
}
/* -- End Navigation Bar -------------------------------------------------------------------- */

// let modalel = document.getElementById("exampleModal");
// let modal = Modal.getInstance(modalel);

// let donateButton = document.getElementById("donate");
// console.log(donateButton);
// donateButton.onclick = function () {
//     console.log("hi");
// }