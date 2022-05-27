const baseURL = 'https://api.podio.com';

function fazPost(url, body) {
    console.log("Body=", body)
    let request = new XMLHttpRequest()
    request.open("POST", url)
    request.setRequestHeader("Content-type", "application/json")
    request.send(JSON.stringify(body))

    return request
}

function fazGet(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url)
    request.send(null)

    return request
}


function autenticaUsuario() {
    event.preventDefault()    
    const oauthTokenEndpoint = '/oauth/token'
    const url = baseURL+oauthTokenEndpoint
    let client_id = document.getElementById("client_id").value
    let client_secret = document.getElementById("client_secret").value
    let username = document.getElementById("username").value
    let password = encodeURIComponent(document.getElementById("password").value)
    console.log("Client ID: "+client_id)
    console.log("Client Secret: "+client_secret)
    console.log("Username: "+username)
    console.log("Password: "+password)

    const requestBody = `?grant_type=password&username=${username}&password=${password}`+
                        `&client_id=${client_id}&client_secret=${client_secret}`
    
    req = fazPost(url+requestBody, "")
    req.onload = function() {
        let resp = this.responseText
        console.log("Response: "+resp)
        if(!resp.includes('error')) {
            document.getElementById("onsuccess").style.display = 'block'
            localStorage.setItem('authentication', resp)
        }
    }
}

function eventoGET(){
    let app_id = document.getElementById("app_id").value
    let item_id = document.getElementById("item_id").value
    let authentication = JSON.parse(localStorage.getItem('authentication'))
    let oauth_token = `?oauth_token=${authentication.access_token}`
    if(app_id && item_id) {
        let appEndpoint = `/app/${app_id}`
        let req1 = fazGet(baseURL+appEndpoint+oauth_token)
        req1.onload = function() {
            let resp = this.responseText
            console.log(resp)
            document.write('<br />=== APP INFO ===<br />'+resp+'<br />')
        }

        let itemEndpoint = `/item/${item_id}`
        let req2 = fazGet(baseURL+itemEndpoint+oauth_token)
        req2.onload = function() {
            let resp = this.responseText
            console.log(resp)
            document.write('<br />=== ITEM INFO ===<br />'+resp+'<br />')
        }
    }else if(app_id) {
        let appEndpoint = `/app/${app_id}`
        let req = fazGet(baseURL+appEndpoint+oauth_token)
        req.onload = function() {
            let resp = this.responseText
            console.log(resp)
            document.write('=== APP INFO ===<br />'+resp)
        }
    }else {
        let itemEndpoint = `/item/${item_id}`
        let req = fazGet(baseURL+itemEndpoint+oauth_token)
        req.onload = function() {
            let resp = this.responseText
            console.log(resp)
            document.write('=== ITEM INFO ===<br />'+resp)
        }
    }
    
}