/* -- Navigation Bar -------------------------------------------------------------------- */
var openMenucategories = document.querySelector(".open-menu-categories");
var categoriesMenu = document.querySelector(".categories");
var selectedcategories = document.querySelector(".selected-categories");
var closeMenucategories = document.querySelector(".close-menu-categories");

openMenucategories.onmouseover = categories;

function categories() {
  close();
  categoriesMenu.style.display = "block";
  selectedcategories.classList.add("selected-rotate");
}

var closer = document.querySelector(".closer");

closeMenucategories.onclick = close;
closer.onmouseover = close;

function close() {
  categoriesMenu.style.display = "none";
  selectedcategories.classList.remove("selected-rotate");
}
/* -- End Navigation Bar -------------------------------------------------------------------- */


/* -- Hero Heading Text Effect -------------------------------------------------------------------- */
var textWrapper = document.querySelector('.hero-heading h1');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({
    loop: false
  })
  .add({
    targets: '.hero-heading h1 .letter',
    opacity: [0, 1],
    easing: "easeInOutQuad",
    duration: 2250,
    delay: (el, i) => 50 * (i + 1)
  });

var textWrapper = document.querySelector('.hero-heading h2');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({
    loop: false
  })
  .add({
    targets: '.hero-heading h2 .letter',
    opacity: [0, 1],
    easing: "easeInOutQuad",
    duration: 1000,
    delay: 4000
  });
/* -- End Hero Heading Text Effect -------------------------------------------------------------------- */


/* -- Counting Numbers Effect -------------------------------------------------------------------- */
document.addEventListener('aos:in:inview', function() {
var intervalId = setInterval(function() {
	var count = $('.count');
	count.text(parseInt(count.text())+1);
}, 50);

setTimeout(function(){
    clearInterval(intervalId);
},3600);});

document.addEventListener('aos:in:inview', function() {
var intervalId1 = setInterval(function() {
	var count1 = $('.count1');
	count1.text(parseInt(count1.text())+1);
  count1.text(parseInt(count1.text())+1);
  count1.text(parseInt(count1.text())+1);
  count1.text(parseInt(count1.text())+1);
  count1.text(parseInt(count1.text())+1);
}, 2);

setTimeout(function(){
    clearInterval(intervalId1);
},3500);});


document.addEventListener('aos:in:inview', function() {
var intervalId2 = setInterval(function() {
	var count2 = $('.count2');
	count2.text(parseInt(count2.text())+1);
  count2.text(parseInt(count2.text())+1);
  count2.text(parseInt(count2.text())+1);
}, 5);

setTimeout(function(){
    clearInterval(intervalId2);
},3500);});


document.addEventListener('aos:in:inview', function() {
var intervalId3 = setInterval(function() {
	var count3 = $('.count3');
	count3.text(parseInt(count3.text())+1);
  count3.text(parseInt(count3.text())+1);
  count3.text(parseInt(count3.text())+1);
}, 50);

setTimeout(function(){
    clearInterval(intervalId3);
},3600);});
/* -- End Counting Numbers Effect -------------------------------------------------------------------- */
