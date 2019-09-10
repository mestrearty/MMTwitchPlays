

function file_exists(name)
	local f= io.open(name, 'r')
	if f ~= nil then
		io.close(f)
		print('deu bom')
		return true
	end
	return false
end

function read_file(name)
	if file_exists(name) then
		local input = io.open(name, 'r')
		if input ~= nil then
			io.input(input)
			local content = io.read()
			io.close(input)
			return content
		end
	end

	return nil
end

function press_button(button)
   local input_table = {}
   input_table[button] = true
   joypad.set(1, input_table)
end

--prev_address=""
--prev_value=""

while true do

	--[[address = read_file('address.txt')
	value = read_file('value.txt')
	if address ~= prev_address and value ~= prev_value then
		hex_address = tonumber(address,16)
		hex_value = tonumber(value, 16)
		if hex_value ~= nil and hex_address ~= nil then
			emu.message(address .. ": ".. value)
			memory.writebyte(hex_address, hex_value)
		end
	end
	prev_address = address
	prev_value = value]]

	if file_exists('button.txt') then
		button = read_file('button.txt')
		os.remove('button.txt')
		emu.message('Pressionando: ' .. button)
		for i=0, 10 do
			press_button(button)

			emu.frameadvance()
		end
    end

	emu.frameadvance()
	gui.text(0,50,"Apenas teste")
end