document.addEventListener( 'DOMContentLoaded', function () {
	new Splide( '#image-slider', {
        'type' : 'loop',
		'fixedHeight': 450,
        'gap': '2em',
        'cover': true,
        'padding': {
            right: '10rem',
            left : '10rem',
        },
        'perPage': 1,
        'autoplay': true
	} ).mount();
} );

$("#MyButton").click(function() {
    alert('Confirm to refresh alert messages.');
    $("#refreshDivID").load("#refreshDivID .reloaded-divs > *");
}); 