f_vals=configureDictionary("double","double");

x_vals=0:0.01:200;
sz=size(x_vals);
for i=1:sz(2)
    s=round(x_vals(i)*100)/100;
    t=real(f(x_vals(i)));
    f_vals=insert(f_vals,s,t,Overwrite=false);
end

f_inverse=dictionary(values(f_vals),keys(f_vals));