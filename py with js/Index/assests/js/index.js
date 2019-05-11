function filechoose(){
    var path = document.getElementById("id1").value
    eel.browsefunc(path)
}

function filechooseagn(){
    var path2 = document.getElementById("id2").value
    eel.browsefunc1(path2)
}

async function finalfunc(){
    let dis = await eel.gofunc()();
    alert(dis);
}
