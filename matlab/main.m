filePattern = fullfile("data\", '*.csv'); 
theFiles = dir(filePattern);
epm_row = [];
acerto_percentual_row = [];
name_row = [];

for k = 1 : length(theFiles)
    baseFileName = theFiles(k).name;
    fullFileName = fullfile(theFiles(k).folder, baseFileName);
    fileName = split(string(baseFileName), ".");
    fprintf(1, 'Now reading %s\n', fullFileName);
    teste = load(fullFileName);
    price_data = teste(:,2:2);
    [epm, acerto_percentual, ys] = previsor(price_data);
    epm_row = [epm_row;epm];
    acerto_percentual_row = [acerto_percentual_row;acerto_percentual];
    name_row = [name_row; fileName(1)];
    ys = [teste((length(price_data) - length(ys) + 1):end,1:1), ys'];
    writematrix(ys,"previsions\" + baseFileName,'Delimiter',',')

end

table(name_row,epm_row,acerto_percentual_row)