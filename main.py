from flask import Flask,render_template,request

viki=Flask(__name__)

@viki.route('/')
def ip():
    return render_template("home.html")

def subnet(ipadd,prelen):
    import math
    
    def a(ipadd,prelen):

        output=''
        output+=('Class:A\n')
        subnetm = '255.'+str((256)-2**(16-prelen))+'.'+'0'+'.'+'0'
        output += (f'subnet mask:{subnetm}\n')
        wdmask = '.'.join(str(255-int(i)) for i in subnetm.split('.'))
        output += (f'wildcard mask:{wdmask}\n')

        ##netwrk id
        msb = 32 - (prelen%32)
        no_of_host = 2**msb
        output += (f'Total num of host:{no_of_host}\n')
        usable_host=no_of_host - 2
        output += (f'usable host:{usable_host}\n')

        avail= [str(int(i)) for i in ipadd.split('.')]
        ##output += (avail[-1])

        last_bit = format(int(avail[-3]),'b')
        ##output += (last_bit)
        borrowed_bits = 24-msb

        if len(last_bit) > 0:
            last_bit_v2 = (''.join('0' for i in range(24-len(last_bit))) + last_bit)[:borrowed_bits]

        last_bit = last_bit_v2 + ''.join('0' for i in range(msb-8))

        def bin_to_deci(x,n):

            dec = 0
            for i in n:
                if x > -1:
                    dec += int(i) * 2**x
                    x -= 1 
            return dec

        nid_lbit = bin_to_deci(7,last_bit_v2)
        
        network_ID = avail[0]+'.'+str(nid_lbit)+'.'+'0'+'.'+'0'
        output += (f'Network id:{network_ID}\n')

        nw_msb=msb%8 
        poss_nw = 2**nw_msb
       
        Start_ip =  avail[0]+'.'+str(nid_lbit)+'.'+str(0)+'.'+str(1)
        output += (f'Start ip:{Start_ip}\n')
        usable_host_range = str(Start_ip + '-' + avail[0]+'.'+str(poss_nw-1))+'.'+'255'+'.'+'254'
        output += (f'usable ip range:{usable_host_range}\n')
        broadcast_id=avail[0]+'.'+str(poss_nw-1)+'.'+'255'+'.'+'255'
        output += (f'broadcast:{broadcast_id}\n')

        zero = 0

        srt_ip =  avail[0]+'.'+str(zero)+'.'+str(zero)+'.'+str(1)
       
        end_ip = str(avail[0]+'.'+str((poss_nw-1)))+'.'+'255'+'.'+'254'
        
        brdcast_id=str(avail[0]+'.'+str((poss_nw-1)))+'.'+'255'+'.'+'255'
        


        r=str(zero)
        nwd_id=avail[0]+'.'+ str(zero)+'.'+ str(zero)+'.'+ str(zero)
        output += ('________________________________________________________________\n|  Network id   |      Start ip  -  End ip      |  Broadcast ip |\n________________________________________________________________\n')
        
        if poss_nw==1:
            end_ip = str(avail[0])+'255.255.254'
            ##print(f'usable ip range:{end_ip}')
            brdcast_id=avail[0]+'.255.255.255'
            output+=(f'|{nwd_id.center(15)}|{srt_ip.center(15)}-{end_ip.center(15)}|{brdcast_id.center(15)}|\n')
            output+=('________________________________________________________________')
            return output
    
    
        else:
            for r in range(0, 255, poss_nw):
                output += (f'|{nwd_id.center(15)}|{srt_ip.center(15)}-{end_ip.center(15)}|{brdcast_id.center(15)}|\n')
                output += ('________________________________________________________________\n')
                nwd_id =avail[0]+'.'+str(r+poss_nw)+'.'+ str(0)+'.'+ str(0)
                srt_ip =  avail[0]+'.'+str(r+poss_nw)+'.'+str(0)+'.'+str(1)
                end_ip =avail[0]+'.'+str(r+poss_nw+(poss_nw-1))+'.'+'255'+'.'+'254'
                brdcast_id=avail[0]+'.'+str(r+poss_nw+(poss_nw-1))+'.'+'255'+'.'+'255'
            return output

    def b(ipadd,prelen):
        output=''
        #subnet and wildcard mask
        output+=('Class:B\n')
        subnetm = '255.255.'+str((256)-2**(24-prelen))+'.'+'0'
        output+=(f'subnet mask:{subnetm}\n')
        wdmask = '.'.join(str(255-int(i)) for i in subnetm.split('.'))
        output+=(f'wildcard mask:{wdmask}\n')

        ##netwrk id
        msb = 16 - (prelen%16)
        no_of_host = 2**msb
        output+=(f'Total num of host:{no_of_host}\n')
        usable_host=no_of_host - 2
        output += (f'usable host:{usable_host}\n')

        avail= [str(int(i)) for i in ipadd.split('.')]
        ##output += (avail[-1])

        last_bit = format(int(avail[-2]),'b')
        ##output += (last_bit)
        borrowed_bits = 16-msb

        if len(last_bit) > 0:
            last_bit_v2 = (''.join('0' for i in range(16-len(last_bit))) + last_bit)[:borrowed_bits]

        last_bit = last_bit_v2 + ''.join('0' for i in range(msb-8))

        def bin_to_deci(x,n):

            dec = 0
            for i in n:
                if x > -1:
                    dec += int(i) * 2**x
                    x -= 1 
            return dec

        nid_lbit = bin_to_deci(7,last_bit_v2)
        ##output += (nid_lbit)
        network_ID = avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(nid_lbit)
        output += (f'Network id:{network_ID}\n')

        ##Start_ip 
        Start_ip =  avail[0]+'.'+avail[1]+'.'+str(nid_lbit)+'.'+str(1)
        output += (f'Start ip:{Start_ip}\n')
        usable_host_range = str(Start_ip + '-' + avail[0]+'.'+avail[1]+'.'+str(nid_lbit+(nid_lbit+1)))+'.'+'254'
        output += (f'usable ip range:{usable_host_range}\n')
        broadcast_id=avail[0]+'.'+avail[1]+'.'+str(nid_lbit+(nid_lbit+1))+'.'+'255'
        output += (f'broadcast:{broadcast_id}\n')

        zero = 0

        nw_msb=msb%8 
        poss_nw = 2**nw_msb
        srt_ip =  avail[0]+'.'+avail[1]+'.'+str(zero)+'.'+str(1)
        ##output += (srt_ip)
        end_ip = str(avail[0]+'.'+avail[1]+'.'+str((poss_nw-1)))+'.'+'254'
        ##output += (f'usable ip range:{end_ip}')
        brdcast_id=avail[0]+'.'+avail[1]+'.'+str((poss_nw-1))+'.'+'255'
        ##output += (f'broadcast:{brdcast_id}')

        r=str(zero)
        nwd_id=avail[0]+'.'+avail[1]+'.'+ str(zero)+'.'+ str(zero)
        output += ('________________________________________________________________\n|  Network id   |      Start ip  -  End ip      |  Broadcast ip |\n________________________________________________________________\n')
        print(output)
        
        if poss_nw==1:
            end_ip = str(avail[0]+'.'+avail[1])+'.255.254'
            ##print(f'usable ip range:{end_ip}')
            brdcast_id=avail[0]+'.'+avail[1]+'.255.255'
            output+=(f'|{nwd_id.center(15)}|{srt_ip.center(15)}-{end_ip.center(15)}|{brdcast_id.center(15)}|\n')
            output+=('________________________________________________________________')
            return output
        else:
            for r in range(0, 255, poss_nw):
                output += (f'|{nwd_id.center(15)}|{srt_ip.center(15)}-{end_ip.center(15)}|{brdcast_id.center(15)}|\n')
                output += ('________________________________________________________________\n')
                nwd_id =avail[0]+'.'+avail[1]+'.'+str(r+poss_nw)+'.'+ str(0)
                srt_ip =  avail[0]+'.'+avail[1]+'.'+str(r+poss_nw)+'.'+str(1)
                end_ip =avail[0]+'.'+avail[1]+'.'+str(r+poss_nw+(poss_nw-1))+'.'+'254'
                brdcast_id=avail[0]+'.'+avail[1]+'.'+str(r+poss_nw+(poss_nw-1))+'.'+'255'
            return output
    def c(ipadd,prelen):
        #subnet and wildcard mask
        output=''
        output += ('Class:C\n')
        subnetm = '255.255.255.'+str((256)-2**(32-prelen))
        output += (f'subnet mask:{subnetm}\n')
        wdmask = '.'.join(str(255-int(i)) for i in subnetm.split('.'))
        output += (f'wildcard mask:{wdmask}\n')

        ##netwrk id
        msb = 8 - (prelen%8)
        no_of_host = 2**msb
        output += (f'Total num of host:{no_of_host}\n')
        usable_host=no_of_host - 2
        output += (f'usable host:{usable_host}\n')
        avail= [str(int(i)) for i in ipadd.split('.')]
        ##output += (avail[-1])

        last_bit = format(int(avail[-1]),'b')
        borrowed_bits = 8-msb

        if len(last_bit) > 0:
            last_bit_v2 = (''.join('0' for i in range(8-len(last_bit))) + last_bit)[:borrowed_bits]

        last_bit = last_bit_v2 + ''.join('0' for i in range(msb))

        def bin_to_deci(x,n):

            dec = 0
            for i in n:
                if x > -1:
                    dec += int(i) * 2**x
                    x -= 1 
            return dec

        nid_lbit = bin_to_deci(7,last_bit)
        ##output += (nid_lbit)
        network_ID = avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(nid_lbit)
        output += (f'Network id:{network_ID}\n')

        ##Start_ip 
        Start_ip =  avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(nid_lbit + 1)
        output += (f'Start ip:{Start_ip}\n')
        usable_host_range = str(Start_ip + '-' + avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(nid_lbit + (usable_host)))
        output += (f'usable ip range:{usable_host_range}\n')
        broadcast_id=str(avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(nid_lbit + (usable_host+1)))
        output += (f'broadcast:{broadcast_id}\n')

        zero = 0

        srt_ip =  avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+ str(zero+1)
        ##output += (srt_ip)
        end_ip = str(avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str( zero + (usable_host)))
        ##output += (f'usable ip range:{end_ip}')
        brdcast_id=str(avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(zero + (usable_host+1)))
        ##output += (f'broadcast:{brdcast_id}')

        r=str(zero)
        nwd_id=avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+ str(zero)
        output += ('________________________________________________________________\n|  Network id   |      Start ip  -  End ip      |  Broadcast ip |\n________________________________________________________________\n')
        
        
        
        for r in range(0, 255, no_of_host):
            output += (f'|{nwd_id.center(15)}|{srt_ip.center(15)}-{end_ip.center(15)}|{brdcast_id.center(15)}|\n')
            output += ('________________________________________________________________\n')
            nwd_id =str(avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+ str( r + (no_of_host)))
            srt_ip =  avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+ str((r + (no_of_host))+1)
            end_ip =avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str(r + (no_of_host) + (usable_host))
            brdcast_id=str(avail[0]+'.'+avail[1]+'.'+avail[2]+'.'+str((r + (no_of_host) + (usable_host)+1)))
        return output

        # lbl = tk.Label(frame, text = "")
    #x=int(input('Enter the class of ip: '))
    prelen=int(prelen)
    ipadd=str(ipadd)
    ab= [str(int(i)) for i in ipadd.split('.')]
    bc=int(ab[0])
    ac=int(ab[1])
    ae=int(ab[2])
    af=int(ab[3])

    if (bc < 128) and  (0 < prelen < 16 and ac<256 and ae<256 and af<256):
        out = a(ipadd,prelen)   
   
    elif (127< bc < 192) and  (15 < prelen < 24 and ae<256 and af<256):
        out = b(ipadd,prelen)  
    
    elif (191 < bc < 224) and  (23 < prelen < 33 and af<256):
        out = c(ipadd,prelen)
    else:
        out='IP RANGE AND CIDR VALUES MISS MATCH\n A CLASS - IP with in Range of 0.0.0.0 - 127.255.255.255 and CIDR in the range of 8-15.\n B CLASS - IP with in Range of 128.0.0.0 - 191.255.255.255 and CIDR in the range of 16-23.\n C CLASS - IP with in Range of 192.0.0.0 - 223.255.255.255 and CIDR in the range of 24-32.\n'
    return out

@viki.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        ip=request.form['ipadd']
        prelen=request.form['prelen']
        out = subnet(ip,prelen)
        out = out.replace('\n','<br>')
        return render_template('result.html',name=out)
    return render_template('home.html')


if __name__=='__main__':        viki.run(host='192.168.1.33',debug=True,port=6010)


