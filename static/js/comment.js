const admin_comments = document.querySelectorAll(".admin-comment-text");
const show_cmt_btns = document.querySelectorAll(".less-more");

for (let i = 0; i < show_cmt_btns.length; i++) {
    let fullText = admin_comments[i].innerText;
    let shortText = fullText.slice(0, 100) + '...';

    if (fullText.length <= 100) {
        show_cmt_btns[i].classList.add("hide");
        continue;
    }

    admin_comments[i].innerText = shortText;
    show_cmt_btns[i].addEventListener("click", (e) => {
        let btn = e.target;

        if (btn.innerText.toLowerCase() === "more") {
            admin_comments[i].innerText = fullText;
            btn.innerText = "less";
        } else {
            admin_comments[i].innerText = shortText;
            btn.innerText = "more";
        }
    });
}