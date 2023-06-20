// function search() {
//     var input = document.getElementById("searchInput").value;
//     if (input === "" || input.replace(/\s/g, "") === "") {
//     } else {
//         window.location.href = `/search/${input.replace(/\s/g, "+")}`;
//     }
// }

function searchSubmit() {
    const searchInput = document.getElementById('searchInput');
    const query = encodeURIComponent(searchInput.value.trim());
    if (query) {
        // Construct the URL based on the search query and submit the form
        // const query = encodeURIComponent(searchInput.value.trim()).replace(/%20/g, '+');
        const searchURL = `/search/${query}`;
        window.location.href = searchURL;
    }
    // Prevent the form from being submitted normally
    return false;
}

function hamburger() {
    document.getElementById("hamburgerDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.hamburgerBtn')) {
        var dropdowns = document.getElementsByClassName("hamburgerContent");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}