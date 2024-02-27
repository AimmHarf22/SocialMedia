document.addEventListener("DOMContentLoaded", function(){
    document.querySelector(".btn-post").addEventListener("click", post_content)

    
   
})

const p = document.createElement("p")
async function post_content() {
    const inputContent = document.querySelector("#js-input-content")
    let inputContentObject = {
        'Post': inputContent.value
    }
    let response = await fetch("/post_api", {
        method: 'POST', 
        body: JSON.stringify(inputContentObject),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
          }

    })
    let e = await response.json()
    console.log(e)


    // ADD POST MESSAGE SUCCESSFULL
    inputContent.value = ''
    p.innerHTML = 'Posted successfully!'
    p.style.margin = '0'
    document.querySelector(".post-element2-container").append(p)

    update_posts()
    

}

async function get_content() {
    let response = await fetch("/get_api")
    let r = await response.json()
    return r
}

function load_posts() {
    get_content().then((response) => {
        const content = response
        const a = JSON.parse(content)
        console.log(a)
        
        for (let i=0; i<a.length; i++) {
            const postContainer = document.querySelector(".all-posts-container2").cloneNode(true)
            postContainer.querySelector("#full-name").innerHTML = `${a[i].fields.first_name} ${a[i].fields.last_name}`
            postContainer.querySelector("#username").innerHTML = `@${a[i].fields.username}`
            postContainer.querySelector(".post-text").innerHTML = `${a[i].fields.post}`
            document.querySelector(".all-posts-container1").append(postContainer)
            // Add to the DOM

        }
    })
    
}


function update_posts() {
    get_content().then((response) => {
        const a = JSON.parse(response)
        const b = a.slice(-1)
        console.log(b)
        const postContainer = document.querySelector(".all-posts-container2").cloneNode(true)
            postContainer.querySelector("#full-name").innerHTML = `${b[0].fields.first_name} ${b[0].fields.last_name}`
            postContainer.querySelector("#username").innerHTML = `@${b[0].fields.username}`
            postContainer.querySelector(".post-text").innerHTML = `${b[0].fields.post}`
            document.querySelector(".all-posts-container1").append(postContainer)
    })
   
}