$(function(){
    $("#copy").click(function(){
        $(this).focus();
        $(this).select();
        document.execCommand("copy");
        $(this).after('copy to clipboard');
    });
});
