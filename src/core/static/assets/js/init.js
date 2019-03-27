$(document).ready(function(){



	//PRELOADER
	$('#prl-img').fadeOut();
	$('#preloader').delay(350).fadeOut('slow');
	console.log('ok');

	//menu

	 $('.hamburger').on('click', function(){
        $(this).find('.bar').toggleClass('active');
        $('#nav_header').toggleClass('active');
    });

	$('.hamburger_sale').on('click', function(){
		$(this).find('.bar_sale').toggleClass('active');
		$('#nav_header_sale').toggleClass('active');
	});

    $('.modal_link').on('click', function(){
        var modal_link = $(this).attr('m-target');
        $(modal_link).addClass('open');
        setTimeout(function() {
            $('html, body').css({'overflow-y': 'hidden'});
        }, 500);
    });
    $('.modal .close').on('click', function(){
        $('.modal').removeClass('open');
        $('html, body').css({'overflow-y': 'auto'});
    });

});

$(document).ready(function(){

	$('a[href^="#"]').on('click',function (e) {
		e.preventDefault();

		var target = this.hash;
		var $target = $(target);

		$('html, body').stop().animate({
			'scrollTop': $target.offset().top
		}, 1000, 'swing', function () {
			window.location.hash = target;
		});
	});
	$('#send').on('click', function() {
		window.open('/files/price.pdf');
	});

	$("#test").innerHTML+='<p>.</p>';
	console.log("hello");

	$(".spoiler-trigger").click(function() {
		$(this).parent().prev().collapse('toggle');
	});
});