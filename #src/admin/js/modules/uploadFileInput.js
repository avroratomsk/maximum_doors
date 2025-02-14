const inputFiles = document.querySelectorAll('.form__controls-file');

const uploadFile  = (e) => {
  const formImages = document.querySelector('.form-images');
  const files = e.currentTarget.files;
  for(let i=0; i < files.length; i++ ){
    const file = files[i];
    formImages.innerHTML += `<img src="/${file.name}" alt="${file.name}">`;
  }
}

inputFiles[0].addEventListener("change", function(event) {
  const file = event.target.files[0]; // Получаем первый файл

  if (file) {
    const reader = new FileReader(); // Создаем FileReader
    reader.onload = function(e) {
      const preview = document.getElementById("imagePreview");
      preview.src = e.target.result; // Устанавливаем превью
      preview.style.display = "block"; // Показываем картинку
    };
    reader.readAsDataURL(file); // Читаем файл как Data URL
  }
});


// inputFiles?.forEach(file => file.addEventListener('change', uploadFile))