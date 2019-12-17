$(function(){
    $("#copypaste").click(function(){
        $(this).focus();
        $(this).select();
        document.execCommand('copypaste');
        $(this).after('copy to clipboard');
    });
});
copyLink =(element) => {
    document.getElementById(element).select();
    document.execCommand("copy");
  };