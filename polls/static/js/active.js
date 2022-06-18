const links = document.querySelectorAll(".menu_item a");


const handleClickLink = (event) => {
    let el = event.target;
    console.log(el)
}

links.forEach(link => {
	link.addEventListener('click', handleClickLink)
})