

document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");
    const posts = document.querySelectorAll(".post-item");

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase();
        // console.log(`Searching for ${query}`)

        posts.forEach(post => {
            const title = post.querySelector(".post-title").innerText.toLowerCase();

            if (title.includes(query)) {
                post.style.display = "";
            } else {
                post.style.display = "none";
            }
        });
    });
});
