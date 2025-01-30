const dropdownItems = document.querySelectorAll(".menu-sidebar__dropdown");

const saveState = (e) => {
  e.currentTarget.classList.toggle("_active");
  const idDropdownItem = e.currentTarget.getAttribute("id");
  if (localStorage.getItem("idDropdownItem") !== idDropdownItem) {
    localStorage.setItem("idDropdownItem", idDropdownItem);
  }
};

const activateStateDropdowmItem = () => {
  const idDropdownItem = localStorage.getItem("idDropdownItem");
  if (idDropdownItem) {
    document.getElementById(idDropdownItem).classList.add("_active");
  }
}

dropdownItems?.forEach(item => item.addEventListener("click", saveState));

activateStateDropdowmItem();


