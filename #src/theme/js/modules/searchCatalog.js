const inputSearch = document.querySelector('input[name="catalog-search"]');

inputSearch?.addEventListener("input", (e) => {
    e.preventDefault();
    if(e.target.value){
        document.getElementById("search-result").style.display = "flex";
    }else{
        document.getElementById("search-result").style.display = "none";
    }
})

document.getElementById("count")?.addEventListener("change", (e) => {
    const count = e.currentTarget.value;
    window.location.search = `?count=${count}`;
})