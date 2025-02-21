const colorSwitchBtns = document.querySelectorAll('.color_btn');

const switchImage = (e) => {
  console.log(e.currentTarget.dataset.src)
}
colorSwitchBtns.forEach(btn => {
  btn.addEventListener('click', switchImage)
})


