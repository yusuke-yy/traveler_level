const url = 'http://127.0.0.1:8000/api/photos/'

const options = {
    method: 'GET'
};

function fetchPhotoImage(url, options){
    return fetch(url, options)
    .then( response => response.json() );
}

async function fetchImage(url, options){
    const response = await fetchPhotoImage(url, options);                     
    // console.log(response[1]);
    // document.getElementById('test').innerHTML = '<a href='+response[0].photo1+'>'+response[0].title+'</a>';
    // document.getElementById('test2').insertAdjacentHTML('afterbegin','<a href='+response[1].photo1+'>'+response[1].title+'</a>');
    
    // for (let i = 0; i <= response.length-1; i++) {
    //     document.getElementById('id').insertAdjacentHTML('afterbegin','<a href=http://127.0.0.1:8000/photo-detail/,'+response[i].id+'/>'+response[i].title+'</a><h2></h2>');
    //     console.log(response.length-1)
    // }
    // for (let i = 0; i <= response.length-1; i++) {
    //     const tag = document.createElement('a');
    //     tag.href = "http://127.0.0.1:8000/photo-detail/,"+response[i].id;
    //     document.body.appendChild(tag);
    //     const imageElement = document.createElement('img');
    //     document.body.appendChild(imageElement);
    //     imageElement.src = response[i].photo1;
    //     imageElement.setAttribute("href","http://127.0.0.1:8000/photo-detail/,"+response[i].id);
    //     // const url = document.getElementById('te'+ response[i].id).insertAdjacentHTML('afterbegin','<a href=http://127.0.0.1:8000/photo-detail/,'+response[i].id+'/>');
    //     // document.body.appendChild(url);
    //     console.log(response.length-1)
    //     imageElement.classList.add("img-photo");
    //     tag.classList.add("tag");
    // }
    for (let i = 0; i <= response.length-1; i++) {
        const tag = document.createElement('a');
        tag.href = "http://127.0.0.1:8000/photo-detail/,"+response[i].id;
        document.body.appendChild(tag);
        tag.setAttribute("id","t"+response[i].id);
        document.getElementById('t'+ response[i].id).insertAdjacentHTML('afterbegin','<img src = '+ response[i].photo1 + ' class = "img-photo"/>');
        console.log(response.length-1)
    }
    // for (let i = 0; i <= response.length-1; i++) {
    //     document.getElementById('te').insertAdjacentHTML('afterbegin','<a href=http://127.0.0.1:8000/photo-detail/,'+response[i].id+'/>');
    // }
}

fetchImage(url,options);
