#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "Audio wrapper interface"

def get_licence():
	return "BSD-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "portaudio"

def get_maintainer():
	return ["Ross Bencina",
	        "Phil Burk"]

def get_version():
	return [19,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	
	my_module.add_src_file([
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
	
	my_module.compile_flags('c', [
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
	
	my_module.compile_version("c", 1999, gnu=True)
	
	my_module.add_path(os.path.join(tools.get_current_path(__file__), 'portaudio/include'))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "portaudio/src/common"))
	my_module.add_header_file([
		'portaudio/include/portaudio.h'
		],
		destination_path="portaudio")
	if target.name=="Windows":
		my_module.add_src_file([
			'portaudio/src/os/win/pa_win_coinitialize.c',
			'portaudio/src/os/win/pa_win_hostapis.c',
			'portaudio/src/os/win/pa_win_waveformat.c',
			'portaudio/src/os/win/pa_win_util.c',
			'portaudio/src/os/win/pa_win_wdmks_utils.c',
			'portaudio/src/os/win/pa_x86_plain_converters.c'
			])
		my_module.add_header_file([
			'portaudio/include/pa_win_waveformat.h',
			'portaudio/include/pa_win_wasapi.h',
			'portaudio/include/pa_win_wdmks.h',
			'portaudio/include/pa_win_wmme.h'
			],
			destination_path="portaudio")
	elif target.name=="Linux":
		my_module.add_optionnal_module_depend('alsa', ["c", "-DPA_USE_ALSA=1"])
		my_module.add_optionnal_module_depend('jack', ["c", "-DPA_USE_JACK=1"])
		my_module.add_optionnal_module_depend('oss', ["c", "-DPA_USE_OSS=1"])
		my_module.add_path(os.path.join(tools.get_current_path(__file__), "portaudio/src/os/unix"))
		my_module.add_src_file([
			'portaudio/src/hostapi/alsa/pa_linux_alsa.c',
			'portaudio/src/hostapi/jack/pa_jack.c',
			'portaudio/src/hostapi/oss/pa_unix_oss.c',
			'portaudio/src/os/unix/pa_unix_hostapis.c',
			'portaudio/src/os/unix/pa_unix_util.c'
			])
		my_module.add_header_file([
			'portaudio/include/pa_jack.h',
			'portaudio/include/pa_linux_alsa.h',
			'portaudio/include/pa_asio.h',
			'portaudio/include/pa_win_ds.h',
			],
			destination_path="portaudio")
	elif target.name=="MacOs":
		my_module.add_path(os.path.join(tools.get_current_path(__file__), "portaudio/src/os/unix"))
		my_module.add_optionnal_module_depend('oss', ["c", "-DPA_USE_COREAUDIO=1"])
		my_module.add_src_file([
			'portaudio/src/hostapi/coreaudio/pa_mac_core.c',
			'portaudio/src/hostapi/coreaudio/pa_mac_core_blocking.c',
			'portaudio/src/hostapi/coreaudio/pa_mac_core_utilities.c',
			'portaudio/src/os/unix/pa_unix_hostapis.c',
			'portaudio/src/os/unix/pa_unix_util.c'
			])
		my_module.add_header_file([
			'portaudio/include/pa_mac_core.h'
			],
			destination_path="portaudio")
	elif target.name=="IOs":
		debug.warning("target for portaudio: " + target.name + " can not be created ... (not supported)");
		return None
	elif target.name=="Android":
		debug.warning("target for portaudio: " + target.name + " can not be created ... (not supported)");
		return None
	else:
		debug.warning("unknow target for portaudio: " + target.name);
	return my_module


