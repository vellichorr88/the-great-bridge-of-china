function [max_shear, max_moment, V_env, M_env] = sweep(P_axle, axle_offsets, x, L, s_values)

    num_locations = length(s_values);
    SFDi = zeros(num_locations, length(x)); % 1 SFD for each train location
    BMDi = zeros(num_locations, length(x)); % 1 BMD for each train location

    for i = 1:num_locations
        s = s_values(i);
        % disp("x = " + s)
        axle_pos = s + axle_offsets;
        on_bridge = (axle_pos >= 0) & (axle_pos <= L);
        if ~any(on_bridge)
            continue
        end
    
        % loads from axles that are actually on the bridge
        P = zeros(1,6);
        for k = 1:6
            if on_bridge(k)
                P(k) = P_axle(k);
            end
        end
    
        % left reaction
        R_A = 0;
        for k = 1:6
            R_A = R_A + P(k) * (L - axle_pos(k)) / L;
        end
        % disp(R_A)
    
        V = R_A * ones(1, length(x));
    
        % shear forces
    
        for k = 1:6
            if on_bridge(k)
                for j = 1:length(x)
                    if x(j) >= axle_pos(k)
                        V(j) = V(j) - P(k);
                    end
                end
            end
        end
    
        % disp("This is V")
        % disp(V)
    
        % moments (area under shear)
        M = R_A * x;
        for k = 1:6
            if on_bridge(k)
                % searched up the statics formula for moment because
                % trapezoidal area was not working
                M = M - P(k) * max(x - axle_pos(k), 0);
            end
        end
    
        % store shear and moment
        SFDi(i,:) = V;
        BMDi(i,:) = M;

    end
    
    % this finds the max shear (abs value) and moment in each row of the SFDi and BMDi
    abs_SFDi = abs(SFDi);
    V_env = max(abs_SFDi, [], 1);
    M_env = max(BMDi, [], 1);
    
    % max shear and max moment in ALL!
    max_shear = max(abs_SFDi, [], "all");
    max_moment = max(BMDi, [], "all");

end

%[appendix]{"version":"1.0"}
%---
