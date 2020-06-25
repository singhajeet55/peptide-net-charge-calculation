amino= int(float(input("enter the no of amino acid: "))) #no of amino acid  in a peptide sequence
for i in range(0,amino):
  
    if i==0:
       
       first_amino_pka=int(float(input("enter the   first_amino_pka: "))) # pka and ph value of side chain for 1st amino acid
       first_amino_ph=int(float(input("enter the first first_amino_ph:")))
       
       first_amino_charge=int(float(input("enter the first first_amino_charge:")))
    
       side_chain= int(float(input("enter the no of side chain: ")))   
       while side_chain > 0 :  
            first_side_chain_pka=int(float(input("enter the   first_side chain_pka: ")))
            first_side_chain_ph=int(float(input("enter the side chain_ph:")))
            break
if first_amino_pka > first_amino_ph:#condition
   protonation = 1
else:
   protonation = -1

while side_chain > 0 :  
   if first_side_chain_pka > first_side_chain_ph:
      side_protonation = 1
   elif first_side_chain_pka < first_side_chain_ph:
      side_protonation = -1
else:
    side_protonation = 0 
       
if i==1:# pka and ph value of side chain for 2nd amino acid
       sec_amino_pka=int(float(input("enter the second_amino_pka: ")))
       sec_amino_ph=int(float(input("enter the se_amino_ph :")))
       sec_amino_charge=int(float(input("enter the se_amino_charge:")))
       sec_side_chain= int(float(input("enter the no of side chain :")))   
       while sec_side_chain > 0 :  
            sec_side_chain_pka=int(float(input("enter the   first_side chain_pka :")))
            sec_side_chain_ph=int(float(input("enter the side chain_ph:")))
            break
if sec_amino_pka > sec_amino_ph:#condition
   sec_protonation = 1
else:
   sec_protonation = -1    

while sec_side_chain > 0 :                   
   if sec_side_chain_pka > sec_side_chain_ph:
      sec_side_protonation= 1
      
   elif sec_side_chain_pka < sec_side_chain_ph:
       sec_side_protonation= -1
   else:
       sec_side_protonation= 0 

       break
net_charge = protonation+sec_protonation+ side_protonation+sec_side_protonation # calculation for net charge
print(net_charge, ':is the net charge of the molecule')



