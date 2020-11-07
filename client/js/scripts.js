function onAnalyser(){

    $("#result").html("")
    $("#loader").show()

    var settings = {
        "async": true,
        "url": "https://classification-lyrics-unip.herokuapp.com/api/v1/classification/band/lyrics",
        "method": "POST",
        "headers": {
          "Content-Type": "application/json",
          "cache-control": "no-cache"
        },
        "data": "{\"lyrics\" : \""+ $("#lyrics").val() + "\" }" 
     }
      
    $.ajax(settings).done(function (response) {
        
        $("#result").html("Esta letra é da banda : " + response.band + ". Probabiidade : " + response.proba)
        $("#loader").hide()
    });

}