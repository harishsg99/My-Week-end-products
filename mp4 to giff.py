import ffmpy
love = ffmpy.FFmpeg(
	inputs = {"video.mp4" : None},
	outputs = {"videp.gif" : None})

love.run