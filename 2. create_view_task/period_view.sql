SELECT periods.id, periods.endpoint_id, mode_start,
  mode_start + mode_duration * '1 minute'::interval AS mode_end,
  mode_duration, label,
  COALESCE((array_agg(distinct reason))[1], '') AS reason,
  COALESCE((array_agg(distinct operator_name))[1], 'Unknown') AS operator_name,
  SUM(kwh) AS energy_sum
FROM public.periods
LEFT JOIN public.reasons ON mode_start=reasons.event_time
LEFT JOIN operators ON
	mode_start > login_time AND
	(mode_start + mode_duration * '1 minute'::interval) < logout_time AND
	operators.endpoint_id = periods.endpoint_id
LEFT JOIN energy ON mode_start <= energy.event_time AND
		(mode_start + mode_duration * '1 minute'::interval) > energy.event_time AND
		energy.endpoint_id = periods.endpoint_id
group by periods.id;
