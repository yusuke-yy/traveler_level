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
    
    for (let i = 0; i <= response.length-1; i++) {
        document.getElementById('id').insertAdjacentHTML('afterbegin','<a href='+response[i].photo1+'>'+response[i].title+'</a><h2></h2>');
        console.log(response.length-1)
    }
}

fetchImage(url,options);
