<?php

function submit($sid, $user, $prob, $lang, $addr, $server = "127.0.0.1", $port = 31415)
{
	$pid = pcntl_fork();
	if ($pid == -1)
		die('could not fork');
	else if ($pid)
		return 0;
	else
	{
		$sock = fsockopen($server, $port);
		$packet = sprintf("%s %s %s %s %s 0", $sid, $user, $prob, $lang, $addr);
		fwrite($sock, $packet);
		fclose($sock);
	}
}

?>
