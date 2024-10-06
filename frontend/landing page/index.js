window.onload = async () =>{
    endpoint = "http://127.0.0.1:8000/api/v1/items_list/"
    response = await fetch(endpoint)
    .then((response)=>(response.json()))
    .then((data)=>(console.log(data)))
    .catch((error)=>(console.log(error.status)))
}
//process.env.FLW_SECRET_KEY