let questions = [];
 
document.addEventListener('htmx:afterRequest', function () {
    let colection = document.getElementsByClassName('question')
    const content = Object.values(colection) 
    for (i = 0; i < content.length; i++){
        questions.push(content[i].innerHTML)

        let word = content[i].innerText
            
        content[i].addEventListener('click', function () {
        if (!questions.includes(word)){
            questions.push(word)
            } else if (questions.includes(word)) {
                const index = questions.indexOf(word);
                if (index !== -1) {
                    questions.splice(index, 1);
                }
            }
        })
    }
})

function toggleIndicator(element) {
  element.classList.toggle("empty");
}

function inputContent () {
    document.getElementById("massaqe-input").value = questions;
};