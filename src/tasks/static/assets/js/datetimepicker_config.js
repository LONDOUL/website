
// DateTimepicker configuration

	$('.form_date').datetimepicker({
		language:  'fr', 
		weekStart: 1,
		todayBtn:  0,
		autoclose: 1,
		todayHighlight: 1,
		startView: 2,
		minView: 2,
		forceParse: 0,
		format: "yyyy-mm-dd",
		pickerPosition:"top-left",
		// pickerPosition:"top-left"
	});
	$('.form_time').datetimepicker({
		language:  'fr',
		weekStart: 1,
		todayBtn:  1,
		autoclose: 1,
		todayHighlight: 1,
		startView: 1,
		minView: 0,
		maxView: 1,
		forceParse: 0,
		format: "hh:ii:ss"
	});

		$('.form_date_2').datetimepicker({
			language:  'fr',
			weekStart: 1,
			todayBtn:  0,
			autoclose: 1,
			todayHighlight: 1,
			startView: 2,
			minView: 2,
			forceParse: 0,
			format: "yyyy-mm-dd",
			// pickerPosition:"top-left",
			pickerPosition:"bottom-left",
			// pickerPosition:"top-left"
		}); 
		$('.form_time_2').datetimepicker({
			language:  'fr',
			weekStart: 1,
			todayBtn:  1,
			autoclose: 1,
			todayHighlight: 1,
			startView: 1,
			minView: 0,
			maxView: 1,
			forceParse: 0,
			format: "hh:ii:ss",
			pickerPosition:"bottom-left",
		});