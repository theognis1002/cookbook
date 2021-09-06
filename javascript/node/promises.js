const customPromise = new Promise((resolve, reject) => {  
    let x = 5;  
    
    if (x > 4) {    
        resolve('Promise is resolved successfully.');  
    } else {    
        reject('Promise is rejected');  
    }
});

customPromise.then((result) => {
    console.log(result);
}).catch((error) => {
    console.log(error);
})
