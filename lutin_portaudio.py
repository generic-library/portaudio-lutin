#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug

def get_desc():
	return "Audio wrapper interface"

def create(target):
	myModule = module.Module(__file__, 'portaudio', 'LIBRARY')
	
	myModule.add_src_file([
		'portaudio/src/common/pa_allocation.c',
		'portaudio/src/common/pa_converters.c',
		'portaudio/src/common/pa_cpuload.c',
		'portaudio/src/common/pa_dither.c',
		'portaudio/src/common/pa_debugprint.c',
		'portaudio/src/common/pa_front.c',
		'portaudio/src/common/pa_process.c',
		'portaudio/src/common/pa_stream.c',
		'portaudio/src/common/pa_trace.c',
		'portaudio/src/hostapi/skeleton/pa_hostapi_skeleton.c',
		'portaudio/src/common/pa_ringbuffer.c'
		])
	
	myModule.compile_flags('c', [
		'-DPA_LITTLE_ENDIAN',
		'-DPACKAGE_NAME=\"\"',
		'-DPACKAGE_TARNAME=\"\"',
		'-DPACKAGE_VERSION=\"\"',
		'-DPACKAGE_STRING=\"\"',
		'-DPACKAGE_BUGREPORT=\"\"',
		'-DPACKAGE_URL=\"\"',
		'-DSTDC_HEADERS=1',
		'-DHAVE_SYS_TYPES_H=1',
		'-DHAVE_SYS_STAT_H=1',
		'-DHAVE_STDLIB_H=1',
		'-DHAVE_STRING_H=1',
		'-DHAVE_MEMORY_H=1',
		'-DHAVE_STRINGS_H=1',
		'-DHAVE_INTTYPES_H=1',
		'-DHAVE_STDINT_H=1',
		'-DHAVE_UNISTD_H=1',
		'-DHAVE_DLFCN_H=1',
		'-DLT_OBJDIR=\".libs/\"',
		'-DHAVE_SYS_SOUNDCARD_H=1',
		'-DHAVE_LINUX_SOUNDCARD_H=1',
		'-DSIZEOF_SHORT=2',
		'-DSIZEOF_INT=4',
		'-DSIZEOF_LONG=8',
		'-DHAVE_CLOCK_GETTIME=1',
		'-DHAVE_NANOSLEEP=1'
		])
	
	myModule.compile_version_CC(1999, gnu=True)
	
	myModule.add_export_path(tools.get_current_path(__file__) + '/portaudio/include')
	myModule.add_path(tools.get_current_path(__file__)+"/portaudio/src/common")
	
	if target.name=="Windows":
		myModule.add_src_file([
			'portaudio/src/os/win/pa_win_coinitialize.c',
			'portaudio/src/os/win/pa_win_hostapis.c',
			'portaudio/src/os/win/pa_win_waveformat.c',
			'portaudio/src/os/win/pa_win_util.c',
			'portaudio/src/os/win/pa_win_wdmks_utils.c',
			'portaudio/src/os/win/pa_x86_plain_converters.c'
			])
	elif target.name=="Linux":
		myModule.add_optionnal_module_depend('alsa', ["c", "-DPA_USE_ALSA=1"])
		myModule.add_optionnal_module_depend('jack', ["c", "-DPA_USE_JACK=1"])
		myModule.add_optionnal_module_depend('oss', ["c", "-DPA_USE_OSS=1"])
		myModule.add_path(tools.get_current_path(__file__)+"/portaudio/src/os/unix")
		myModule.add_src_file([
			'portaudio/src/hostapi/alsa/pa_linux_alsa.c',
			'portaudio/src/hostapi/jack/pa_jack.c',
			'portaudio/src/hostapi/oss/pa_unix_oss.c',
			'portaudio/src/os/unix/pa_unix_hostapis.c',
			'portaudio/src/os/unix/pa_unix_util.c'
			])
	elif target.name=="MacOs":
		myModule.add_path(tools.get_current_path(__file__)+"/portaudio/src/os/unix")
		myModule.add_optionnal_module_depend('oss', ["c", "-DPA_USE_COREAUDIO=1"])
		myModule.add_src_file([
			'portaudio/src/hostapi/coreaudio/pa_mac_core.c',
			'portaudio/src/hostapi/coreaudio/pa_mac_core_blocking.c',
			'portaudio/src/hostapi/coreaudio/pa_mac_core_utilities.c',
			'portaudio/src/os/unix/pa_unix_hostapis.c',
			'portaudio/src/os/unix/pa_unix_util.c'
			])
	elif target.name=="IOs":
		debug.warning("target for portaudio: " + target.name + " can not be created ... (not supported)");
		return None
	elif target.name=="Android":
		debug.warning("target for portaudio: " + target.name + " can not be created ... (not supported)");
		return None
	else:
		debug.warning("unknow target for portaudio: " + target.name);
	return myModule


