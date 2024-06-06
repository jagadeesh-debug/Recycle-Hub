document.getElementById("menu").addEventListener('click', function () {
    const button = document.getElementById("menu");

    const src = button.getAttribute('xlmns');

    if (src === "http://www.w3.org/2000/svg") {
        button.setAttribute("src", "./assets/cancel.png");
        const nav = document.createElement('div');
        nav.innerHTML = `<a href="">Home</a>
        <a href="">Products</a>
        <a href="">About</a>
        <a href="">Contact Us</a>`;
        nav.setAttribute('id', 'navList');
        document.body.appendChild(nav);
        setTimeout(() => {
            nav.classList.add('show');
        }, 100);
    } else {
        button.setAttribute("xmlns","http://www.w3.org/2000/svg");
        const nav = document.getElementById("navList");
        nav.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(nav);
        }, 300);
    }
}); 


function navtoIndex(){
    window.location.href = "index.html"
}

function navtoPickUp(){
    window.location.href = "PickUp.html"
}
